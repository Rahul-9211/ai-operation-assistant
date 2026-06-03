from app.classes.identity import Identity


class IdentityService:

    def create_identity(self, request: Identity):
        print("Creating identity", request);
        return {"message": "Hello, World!sss", "request": request}