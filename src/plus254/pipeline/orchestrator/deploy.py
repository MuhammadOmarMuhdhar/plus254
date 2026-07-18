import logging

from plus254.pipeline.orchestrator.flows import (
    fixed_source_flow,
    rolling_source_flow,
    static_source_flow,
)

logger = logging.getLogger(__name__)


def deploy_all():
    """Create deployments for all source types and frequencies."""

    logger.info("Deploying fixed-source-monthly …")
    fixed_source_flow.deploy(
        name="fixed-source-monthly",
        parameters={"frequency": "monthly", "dry_run": False},
        cron="0 2 1 * *",
        work_pool_name="plus254-pool",
    )

    logger.info("Deploying fixed-source-quarterly …")
    fixed_source_flow.deploy(
        name="fixed-source-quarterly",
        parameters={"frequency": "quarterly", "dry_run": False},
        cron="0 2 1 1,4,7,10 *",
        work_pool_name="plus254-pool",
    )

    logger.info("Deploying fixed-source-annually …")
    fixed_source_flow.deploy(
        name="fixed-source-annually",
        parameters={"frequency": "annually", "dry_run": False},
        cron="0 2 1 1 *",
        work_pool_name="plus254-pool",
    )

    logger.info("Deploying static-source-manual …")
    static_source_flow.deploy(
        name="static-source-manual",
        parameters={"dry_run": False},
        work_pool_name="plus254-pool",
    )

    logger.info("Deploying rolling-source-ca-quarterly …")
    rolling_source_flow.deploy(
        name="rolling-source-ca-quarterly",
        parameters={"source": "ca", "dry_run": False},
        cron="0 2 15 1,4,7,10 *",
        work_pool_name="plus254-pool",
    )

    logger.info("All deployments created successfully.")


if __name__ == "__main__":
    deploy_all()