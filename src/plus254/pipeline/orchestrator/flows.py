from prefect import flow

from plus254.pipeline.orchestrator import registry, tasks


@flow(name="fixed-source-etl")
def fixed_source_flow(
    frequency: str | None = None,
    dry_run: bool = False,
):
    """Run all fixed-source datasets."""
    slugs = registry.get_slugs(
        "src/plus254/datasets.yaml",
        source_type="fixed",
        frequency=frequency,
    )

    for slug in slugs:
        tasks.run_fixed_source(slug, dry_run=dry_run)


@flow(name="static-source-etl")
def static_source_flow(dry_run: bool = False):
    """Run static (one-time) datasets."""
    slugs = registry.get_slugs(
        "src/plus254/datasets.yaml",
        source_type="static",
    )

    for slug in slugs:
        tasks.run_static_source(slug, dry_run=dry_run)


@flow(name="rolling-source-etl")
def rolling_source_flow(
    source: str,
    dry_run: bool = False,
):
    """Run all datasets from a rolling source. """

    all_records = tasks.extract_rolling_source(source)
    slugs = registry.get_slugs(
        "src/plus254/datasets.yaml",
        source_type=f"rolling_{source}",
    )
    for slug in slugs:
        slug_records = [r for r in all_records if r.get("dataset") == slug]
        if slug_records:
            tasks.run_rolling_slug(slug, slug_records, dry_run=dry_run)