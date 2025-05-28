class TimingMiddleware:
    async def __call__(self, request: Request, call_next: Callable) -> Response:
        start_time = datetime.utcnow()
        response = await call_next(request)
        process_time = (datetime.utcnow() - start_time).total_seconds() * 1000
        response.headers["X-Process-Time"] = str(process_time)
        return response