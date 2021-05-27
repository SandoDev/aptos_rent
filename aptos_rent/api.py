from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/")
def root(request):
    return {"message": "api of aptos rent"}
