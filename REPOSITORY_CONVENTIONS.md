# Repository Conventions

## Target Repository Type

This is a Git-backed Markdown documentation repository.

Treat it as a versioned documentation product, not a loose note pile.

## File Naming

Use:

- uppercase snake case for major top-level guidance docs: `MANAGEMENT_PRACTICES_OVERVIEW.md`
- lowercase kebab case for reusable templates: `templates/project-brief.md`
- uppercase snake case for discipline guides: `disciplines/PEOPLE_MANAGEMENT.md`
- descriptive names over cute names

Avoid:

- spaces in file names
- vague names like `notes.md`, `misc.md`, or `new.md`
- date-stamped files unless the document is actually time-bound

## Document Structure

Major guidance docs should normally include:

- `# Title`
- `## Purpose`
- audience or scope where useful
- key practices or guidance
- decision rules / review gates where relevant
- artifacts/templates where relevant
- anti-patterns
- related links

Not every file needs every section. But if a guide cannot explain its purpose, it is probably not ready to exist in public without adult supervision.

## Linking Standard

For README and public/navigation documents, use absolute GitHub links:

`https://github.com/RusDavies/docs-management-practices/blob/master/path/to/file.md`

For internal drafting inside a doc, relative links may be acceptable, but prefer GitHub links when the document is likely to be read outside the repository checkout.

When renaming or adding files:

- update `README.md`
- update `DOCUMENT_MAP.md`
- update related audience/discipline guides
- update TODO/backlog if follow-up work appears

## Source and Permissions Standard

Do not copy or closely paraphrase third-party material without tracking it.

Use [Source and Permissions Register](https://github.com/RusDavies/docs-management-practices/blob/master/SOURCE_AND_PERMISSIONS_REGISTER.md) for:

- quoted material
- adapted frameworks
- copied tables or diagrams
- externally sourced definitions
- licensed content
- permissions assumptions
- inspiration that may require attribution or caution

Lencioni's model may be discussed as inspiration, but the guidance should stand in its own voice and avoid becoming a derivative summary of proprietary material.

## Source Anchors and Retrieval Structure

Some discipline guides are mapped by the downstream [agent-specialist-registry](https://github.com/RusDavies/agent-specialist-registry/blob/master/README.md) repository. That repository generates or validates agent task packs, retrieval chunks, eval scenarios, review gates, and drift checks from stable source anchors in this canonical human-readable corpus.

When a discipline guide is or may become part of that downstream mapping:

- include a stable doctrine marker near the top of the mapped block, normally immediately after the `#` title: `<!-- doctrine:id=discipline-slug -->`
- use lowercase kebab-case anchor ids that match the discipline or mapped concept, such as `project-management`
- do not rename, remove, duplicate, or casually move existing `doctrine:id` markers; downstream drift checks depend on them
- treat the text from a doctrine marker until the next doctrine marker, or end of file, as a hash-tracked source block
- use additional doctrine markers only when a downstream artifact intentionally maps to multiple stable blocks
- keep second-level `##` headings meaningful because downstream generation extracts section titles for task-pack source coverage
- keep the opening sections self-contained enough to work as retrieval context; generated retrieval chunks currently include source extracts, not a rewritten doctrine layer
- prefer additive, scoped edits over restructuring mapped blocks unless the downstream artifacts will be regenerated and reviewed
- when materially changing a mapped block, expect `agent-specialist-registry` drift checks to fail until its generated manifest/artifacts are refreshed

The human guidance remains canonical. Source anchors are not agent instructions and should not make the prose less readable for humans. They are alignment handles: tiny boring comments that prevent future-us from debugging doctrine drift with a shovel.

## AI-Assisted Writing Standard

AI assistance is allowed for drafting, structure, review, consistency checks, and quality gates.

Rules:

- human owner remains responsible for final content
- factual claims must be checked against real sources
- AI summaries are working notes, not sources
- sensitive/public-facing material must pass publication gates
- do not paste confidential/private employer material into prompts without explicit approval and an allowed tool/provider context

If AI assistance is material to a durable artifact, review, evidence synthesis, repository-maintenance action, or publication-sensitive decision, record it using [AI Use Register and Disclosure Posture](AI_USE_REGISTER_AND_DISCLOSURE.md) and the [AI Use Register](templates/ai-use-register.md).

If a public version is prepared, decide whether AI-use disclosure is needed for that publication context and record the rationale.

## Voice and Style

Default voice:

- practical
- direct
- human
- slightly dry when useful
- concrete over abstract
- management as operating discipline, not leadership theatre

Avoid:

- corporate fog
- motivational wallpaper
- jargon without decision value
- sterile role-label mush when a human example would read better
- culture-war framing unless explicitly approved

Use [Writing Style Guidance](https://github.com/RusDavies/docs-management-practices/blob/master/WRITING_STYLE_GUIDANCE.md) for public-brand/persona/example guidance.

## Review Expectations

Before merging meaningful documentation changes:

- run `git diff --check`
- verify required files exist
- verify README/document-map links when navigation changes
- verify no placeholder TODOs remain in completed docs
- verify sensitive sections are gated
- update TODO/backlog and memory when meaningful

## Git Workflow

Use branch-per-work-item:

1. Create a branch from clean `master`.
2. Make scoped changes.
3. Verify.
4. Commit.
5. Merge back to `master`.
6. Push to `origin/master`.

Keep commits scoped. Do not sweep unrelated workspace edits into project commits. Future-us has suffered enough.
