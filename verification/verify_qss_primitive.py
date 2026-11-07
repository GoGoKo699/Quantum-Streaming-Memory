"""Finite Choi-state verification of the inherited F4 (2,3) QSS primitive.

This checks the actual coherent state, including reference and recycled pair;
it does not establish the streaming schedule or the universal converse.
"""
import json
from pathlib import Path
import numpy as np


def add(a, b):
    return a ^ b


def mul(a, b):
    c = 0
    for _ in range(2):
        if b & 1:
            c ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7  # x^2+x+1
    return c


def inv(a):
    return next(b for b in range(1, 4) if mul(a, b) == 1)


q, alpha = 4, 2
encoder_images = {(add(r, s), add(r, mul(alpha, s)))
                  for s in range(q) for r in range(q)}
assert len(encoder_images) == q * q

# Normalized Choi purification in register order R,Q,A,C.
psi = np.zeros((q, q, q, q), dtype=complex)
for s in range(q):
    for r in range(q):
        psi[s, r, add(r, s), add(r, mul(alpha, s))] = 1 / q
assert np.isclose(np.vdot(psi, psi), 1)

target = np.zeros((q, q, q, q), dtype=complex)
for s in range(q):
    for j in range(q):
        target[s, s, j, j] = 1 / q  # Bell(R,O) tensor Bell(J,erased)

checks = []
for erased in ['C', 'A', 'Q']:
    actual = np.zeros_like(target)
    images = set()
    for x in range(q):
        for y in range(q):
            if erased == 'C':  # received Q=x,A=y
                s = add(y, x)
                j = add(x, mul(alpha, s))
            elif erased == 'A':  # received Q=x,C=y
                s = mul(add(y, x), inv(alpha))
                j = add(x, s)
            else:  # received A=x,C=y
                s = mul(add(y, x), inv(add(alpha, 1)))
                j = add(x, s)
            images.add((s, j))
            for ref in range(q):
                for lost in range(q):
                    original = (ref, x, y, lost) if erased == 'C' else (
                        (ref, x, lost, y) if erased == 'A' else (ref, lost, x, y))
                    actual[ref, s, j, lost] += psi[original]
    assert len(images) == q * q
    fidelity = float(abs(np.vdot(target, actual)) ** 2)
    error = float(np.max(np.abs(actual - target)))
    assert error < 1e-12
    checks.append({'erased_share': erased,
                   'decoder_is_basis_permutation': True,
                   'choi_output_and_syndrome_fidelity': fidelity,
                   'max_amplitude_error': error})

# Each individual transmitted share has no information about the source.
for share_axis, name in [(1, 'Q'), (2, 'A'), (3, 'C')]:
    others = [i for i in range(4) if i not in [0, share_axis]]
    matrix = np.transpose(psi, [0, share_axis] + others).reshape(q*q, q*q)
    rho = matrix @ matrix.conj().T
    assert np.allclose(rho, np.eye(q*q)/(q*q))

result = {
    'scope': 'Inherited F4 QSS encoder, all single-share erasures, and recycled entanglement',
    'physical_grouping': 'One ququart is two physical qubits; fixed alphabet independent of B,D',
    'checks': checks,
    'each_single_share_independent_of_reference': True,
    'successful_QA_decoding_returns_exact_EPR_with_sender_C': True,
    'limitations': 'Finite algebra check; no theorem, literature priority, or schedule certification'
}
Path(__file__).with_name("qss_primitive_verification.json").write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
