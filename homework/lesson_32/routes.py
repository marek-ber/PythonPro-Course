# 19. 🧠 (Challenge) Refaktoryzacja - Organizacja Tras: (Znacie aplikacje Django). Zamiast
# dodawać wszystkie trasy w create_app() , stwórz osobną funkcję (np.
# setup_routes(app) ) w osobnym pliku routes.py . Zaimportuj ją i wywołaj w
# create_app . To poprawia czytelność dużych projektów.


from handlers import (
    add_product,
    chat,
    create_account,
    create_user,
    delete_product,
    get_all_products,
    get_single_product,
    transfer,
    update_product,
)


def setup_routes(app):
    app.router.add_post("/products", add_product)
    app.router.add_get("/products", get_all_products)
    app.router.add_get("/products/{id}", get_single_product)
    app.router.add_put("/products/{id}", update_product)
    app.router.add_patch("/products/{id}", update_product)
    app.router.add_delete("/products/{id}", delete_product)

    app.router.add_post("/users", create_user)
    app.router.add_post("/accounts", create_account)
    app.router.add_post("/transfer", transfer)

    app.router.add_post("/api/v1/chat", chat)
