from .main import root 

def main():
    """CLI entry point"""
    root(auto_envvar_prefix='ECS')

main()