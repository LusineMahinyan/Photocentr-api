import { Link } from "react-router-dom";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

function HomePage() {
    return (
        <>
            <Navbar />

            <main>

                <section className="container py-5">

                    <div className="row align-items-center">

                        <div className="col-lg-6">

                            <h1 className="display-3 fw-bold">
                                Фотоцентр
                                <br />
                                <span className="text-warning">
                                    «Слоник»
                                </span>
                            </h1>

                            <p className="lead mt-4">
                                Быстрая печать фотографий, фото на документы,
                                ламинирование и другие услуги.
                            </p>

                            <Link
                                to="/services"
                                className="btn btn-warning btn-lg mt-3"
                            >
                                Посмотреть услуги
                            </Link>

                        </div>


                        <div className="col-lg-6 text-center">

                            <img
                                src="/slonik.png"
                                alt="Фотоцентр Слоник"
                                className="img-fluid"
                                style={{
                                    maxHeight: "450px"
                                }}
                            />

                        </div>

                    </div>

                </section>

            </main>

            <Footer />
        </>
    );
}

export default HomePage;
