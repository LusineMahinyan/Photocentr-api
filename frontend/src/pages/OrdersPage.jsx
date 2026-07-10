import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

import { getMyOrders } from "../api/orders";


function OrdersPage() {

    const [orders, setOrders] = useState([]);


    useEffect(() => {

        loadOrders();

    }, []);



    async function loadOrders() {

        try {

            const data = await getMyOrders();


            console.log(
                "ЗАКАЗЫ С СЕРВЕРА:",
                data
            );


            setOrders(data);


        } catch (error) {

            console.error(
                "ОШИБКА ЗАКАЗОВ:",
                error.response?.data || error.message
            );

        }

    }



    function statusText(status) {

        const statuses = {

            new: "🟡 Новый",

            processing: "🔵 В обработке",

            ready: "🟢 Готов",

            completed: "✅ Выполнен",

            cancelled: "❌ Отменён"

        };


        return statuses[status] || status;

    }



    return (

        <>

            <Navbar />


            <div className="container py-5">


                <h1 className="fw-bold mb-4">
                    📦 Мои заказы
                </h1>



                {
                    orders.length === 0 ? (

                        <div className="alert alert-info">

                            У вас пока нет заказов

                        </div>


                    ) : (


                        orders.map((order) => (

                            <div
                                className="card shadow-sm mb-4"
                                key={order.id}
                            >

                                <div className="card-body">


                                    <h4>
                                        Заказ №{order.id}
                                    </h4>


                                    <p>
                                        Статус:
                                        {" "}
                                        <b>
                                            {statusText(order.status)}
                                        </b>
                                    </p>


                                    <p>
                                        Сумма:
                                        {" "}
                                        {order.total_price} ₽
                                    </p>


                                    <p>
                                        Дата:
                                        {" "}
                                        {new Date(
                                            order.created_at
                                        ).toLocaleString()}
                                    </p>


                                    <hr />


                                    <h5>
                                        Услуги:
                                    </h5>


                                    {
                                        order.items.map((item) => (

                                            <div key={item.id}>

                                                Услуга №{item.service_id}

                                                {" — "}

                                                {item.price} ₽

                                            </div>

                                        ))
                                    }


                                </div>


                            </div>

                        ))

                    )
                }


            </div>


            <Footer />

        </>

    );

}


export default OrdersPage;
