# Check the mathematics displayed by GitHub

The [hosted-math workflow](../../.github/workflows/hosted-math.yml) compares the mathematics on actual, commit-pinned GitHub pages with the corresponding source expressions. It runs with read-only repository permission, uses a fresh unsigned-in browser, and uploads the diagnostic captures as a workflow artifact. It checks all tracked Markdown pages at viewport widths of 1440 and 760 pixels.

The collector inventories inline and display mathematics, compiles the source to expected MathML, and compares that structure with the hosted MathML. It checks expression counts, subscripts, fractions, relations, visible labels and bounded display geometry. The [explicit text contract](../hosted/math-contract.json) additionally protects the main memory law and the strict inequality in the README's feedback table. A source edit that moves or changes these expressions requires a corresponding deliberate contract update.

## Reproduce a capture

Use Node.js 18 or newer, Python 3.10 or newer, Git, Playwright and MathJax. Install browser dependencies in a temporary directory outside the repository. For example:

```bash
npm install --prefix /tmp/streaming-math-deps playwright@1.56.1 mathjax-full@3.2.1
/tmp/streaming-math-deps/node_modules/.bin/playwright install chromium
NODE_PATH=/tmp/streaming-math-deps/node_modules node verification/hosted/capture_hosted_math.cjs \
  --root "$PWD" \
  --repository GoGoKo699/Quantum-Streaming-Memory \
  --revision FULL_40_CHARACTER_COMMIT \
  --contract verification/hosted/math-contract.json \
  --output /tmp/streaming-math-capture
```

Replace the revision with the actual full commit SHA and use a new empty output directory for every attempt. The collector reads Git objects at that revision, so uncommitted changes are excluded. The corresponding commit must be available on public GitHub. Restricted networks or browser runtimes may prevent capture; that is an unperformed hosted check, not a pass.

## Interpret the evidence

`hosted-report.json` records the repository, commit, tree, source hashes, complete page and expression scope, two viewport results and artifact hashes. Its supporting files include the expected and actual mathematics, HTML, screenshots and diagnostics. Failed attempts remain useful evidence and should be retained separately from later successful captures.

An automated pass does not inspect every pixel or establish the scientific result. Review the actual screenshots of the principal claims, proofs, learning route and every flagged or repaired expression at both widths. Check navigation and prose separately. These observations concern the captured GitHub renderer and revision; they do not certify future rendering, every browser, literature priority or proof validity. Workflow artifacts expire, so preserve the report and important review findings when a lasting record is needed.

Return to the [scientific verification account](../README.md).
