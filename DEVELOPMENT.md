# Developing SCUTER

## Source files

Maintain the protocol in `protocol/01.work-contract.md`. The instruction entry point is `skills/scuter/SKILL.md`. The implementation guide, Notion setup guidance, and record/review guidance are maintained in `docs/`. `VERSION` and the Skill metadata must agree.

The files under `skills/scuter/references/`, the Skill manifest, and `dist/` are generated. Do not edit them separately. The manifest identifies local source files and their SHA-256 hashes. Git records the exact repository revision associated with each committed distribution.

## Build and check

Python 3.10 or newer is the only build requirement. No package installation, network access, credentials, other repository, or external service is needed.

```bash
python3 tools/build.py
python3 tools/build.py --check
python3 -m unittest discover -s tests -v
```

The build produces a Skill archive with a `scuter/` root directory, a complete Markdown instruction edition, companion files, a manifest, and `dist/SHA256SUMS`. It uses sorted archive entries, fixed timestamps, fixed file permissions, and uncompressed ZIP storage for byte-reproducible packaging independent of compression-library versions.

`--check` writes nothing. It compares the checked-in generated files against outputs derived from the current local sources and validates archive contents. The tests exercise repeatability, content hashes, changed sources, version mismatches, missing companions, unexpected files, symlinks, and corrupted artifacts.

Commit a source revision and its regenerated distributions together. Review substantive protocol changes separately from packaging changes. A new source or package version requires a recorded User decision before formal release.

## Application testing

Packaging tests are distinct from application testing. Record the application and interface, date, displayed model/version when available, installation route, access to companion files, available shared-record integration, and completion of a task-review-acceptance cycle. A successful file upload establishes only file intake.

The project record should state what was actually tested, what failed, and what remains uncertain. Do not infer support for one product from support in a similarly named product.
