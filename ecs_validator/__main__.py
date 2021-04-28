from .main import root


def main():
    """CLI entry point"""
    root(prog_name="ecs_validator", auto_envvar_prefix='ECS')


main()
