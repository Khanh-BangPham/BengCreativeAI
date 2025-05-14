from git_changelog.cli import build_and_render

build_and_render(
    repository=".",
    output="CHANGELOG.md",
    convention="angular",
    provider="github",
    template="keepachangelog",
    parse_trailers=True,
    parse_refs=False,
    sections=["build", "deps", "feat", "fix", "refactor"],
    versioning="pep440",
    bump="1.1.2", 
    in_place=True,
)
