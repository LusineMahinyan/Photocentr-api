import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

import {
    getCart,
    removeFromCart,
    clearCart
} from "../api/cart";

import { checkoutOrder } from "../api/orders";


function CartPage() {

    const [cart, setCart] = useState(null);


    useEffect(() => {
        loadCart();
    }, []);


    async function loadCart() {

        try {

            const data = await getCart();

            setCart(data);


        } catch (error) {

            console.error(
                "Ошибка загрузки корзины:",
                error.response?.data || error.message
            );

        }

    }



    async function handleRemove(item) {

        console.log(
            "Удаляем:",
            item
        );


        const id = item.id;


        if (!id) {

            alert(
                "Нет ID элемента корзины"
            );

            return;

        }


        try {

            await removeFromCart(id);

            await loadCart();


        } catch (error) {

            console.error(
                "Ошибка удаления:",
                error.response?.data || error.message
            );

        }

    }



    async function handleClearCart() {

        try {

            await clearCart();

            await loadCart();


        } catch (error) {

            console.error(
                "Ошибка очистки:",
                error.response?.data || error.message
            );

        }

    }



    async function handleCheckout() {

        try {


            const order = await checkoutOrder();


            console.log(
                "Создан заказ:",
                order
            );


            alert(
                "Заказ успешно оформлен!"
            );


            await loadCart();



        } catch (error) {


            console.error(
                "Ошибка оформления заказа:",
                error.response?.data || error.message
            );


            alert(
                JSON.stringify(
                    error.response?.data || error.message
                )
            );

        }

    }



    function getServiceName(item) {

        return (
            item.service?.name ||
            item.name ||
            item.service_name ||
            `Услуга №${item.service_id}`
        );

    }



    function getServicePrice(item) {

        return Number(
            item.price || 0
        );

    }



    const items = cart?.items || [];


    const total = items.reduce(
        (sum, item) =>
            sum + getServicePrice(item),
        0
    );



    return (

        <>

            <Navbar />


            <div className="container py-5">


                <h1 className="fw-bold mb-4">
                    🛒 Корзина
                </h1>



                {
                    items.length === 0 ? (

                        <div className="alert alert-info">

                            Ваша корзина пока пуста

                        </div>


                    ) : (


                        <>


                            <div className="row">


                                {
                                    items.map((item) => (

                                        <div
                                            className="col-md-6 mb-4"
                                            key={item.id}
                                        >

                                            <div className="card shadow-sm">

                                                <div className="card-body">


                                                    <h4>
                                                        {getServiceName(item)}
                                                    </h4>


                                                    <p>
                                                        Цена: {getServicePrice(item)} ₽
                                                    </p>


                                                    <button
                                                        className="btn btn-danger"
                                                        onClick={() => handleRemove(item)}
                                                    >

                                                        Удалить

                                                    </button>


                                                </div>

                                            </div>

                                        </div>

                                    ))
                                }


                            </div>



                            <div className="card shadow-sm mt-4">


                                <div className="card-body">


                                    <h4>
                                        Итого: {total} ₽
                                    </h4>



                                    <button
                                        className="btn btn-outline-danger me-3"
                                        onClick={handleClearCart}
                                    >

                                        Очистить корзину

                                    </button>



                                    <button
                                        className="btn btn-warning"
                                        onClick={handleCheckout}
                                    >

                                        Оформить заказ

                                    </button>



                                </div>


                            </div>


                        </>


                    )

                }


            </div>


            <Footer />

        </>

    );

}


export default CartPage;
