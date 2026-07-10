import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

import { getServices } from "../api/services";
import { addToCart } from "../api/cart";


function ServicesPage() {

    const [services, setServices] = useState([]);


    useEffect(() => {
        loadServices();
    }, []);


    async function loadServices() {

        try {

            const data = await getServices();

            console.log("Услуги:", data);

            setServices(data);

        } catch (error) {

            console.error("Ошибка:", error);

        }

    }


    async function handleAddToCart(serviceId) {

        try {

            await addToCart(serviceId);

            alert("Услуга добавлена в корзину 🛒");

        } catch (error) {

            console.error("Ошибка корзины:", error);

            alert(
                "Необходимо войти в аккаунт, чтобы добавить услугу в корзину"
            );

        }

    }


    return (
        <>

            <Navbar />


            <div className="container py-5">


                <h1 className="mb-4 fw-bold">
                    Наши услуги
                </h1>


                <div className="row">


                    {services.map((service) => (


                        <div
                            className="col-md-4 mb-4"
                            key={service.id}
                        >


                            <div className="card h-100 shadow-sm">


                                <div className="card-body">


                                    <h4 className="card-title">
                                        {service.name}
                                    </h4>


                                    <p className="card-text">
                                        {service.description}
                                    </p>


                                </div>


                                <div className="card-footer bg-white d-flex justify-content-between align-items-center">


                                    <strong className="fs-5">
                                        {service.price} ₽
                                    </strong>


                                    <button
                                        className="btn btn-warning"
                                        onClick={() => handleAddToCart(service.id)}
                                    >
                                        🛒 В корзину
                                    </button>


                                </div>


                            </div>


                        </div>


                    ))}


                </div>


            </div>


            <Footer />


        </>
    );
}


export default ServicesPage;
