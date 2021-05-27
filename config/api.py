from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/", tags=["Meta"])
def root(request):
    return {"message": "api of aptos rent"}
