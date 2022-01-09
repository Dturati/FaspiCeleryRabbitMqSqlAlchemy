import uvicorn



def main() -> None:
    """Entrypoint of the application.py."""
    uvicorn.run(
        "application:create_app",
        factory=True,
        reload=True
    )


if __name__ == "__main__":
    main()
