import { Link, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";


function Navbar() {

    const navigate = useNavigate();


    const [token, setToken] = useState(
        localStorage.getItem("access_token")
    );


    useEffect(() => {

        const checkToken = () => {

            setToken(
                localStorage.getItem("access_token")
            );

        };


        window.addEventListener(
            "storage",
            checkToken
        );


        return () => {

            window.removeEventListener(
                "storage",
                checkToken
            );

        };

    }, []);



    function logout() {

        localStorage.removeItem(
            "access_token"
        );


        setToken(null);


        navigate("/");

    }



    return (

        <nav className="navbar navbar-expand-lg bg-white shadow-sm">

            <div className="container">


                <Link
                    className="navbar-brand fw-bold fs-3 text-warning"
                    to="/"
                >
                    🐘 Слоник
                </Link>



                <button
                    className="navbar-toggler"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#navbarMenu"
                >

                    <span className="navbar-toggler-icon"></span>

                </button>



                <div
                    className="collapse navbar-collapse"
                    id="navbarMenu"
                >


                    <ul className="navbar-nav ms-auto">


                        <li className="nav-item">

                            <Link
                                className="nav-link"
                                to="/"
                            >
                                Главная
                            </Link>

                        </li>



                        <li className="nav-item">

                            <Link
                                className="nav-link"
                                to="/services"
                            >
                                Услуги
                            </Link>

                        </li>



                        <li className="nav-item">

                            <Link
                                className="nav-link"
                                to="/cart"
                            >
                                🛒 Корзина
                            </Link>

                        </li>



                        {
                            token ? (

                                <>


                                    <li className="nav-item">

                                        <Link
                                            className="nav-link"
                                            to="/orders"
                                        >
                                            📦 Мои заказы
                                        </Link>

                                    </li>



                                    <li className="nav-item">

                                        <Link
                                            className="nav-link"
                                            to="/profile"
                                        >
                                            👤 Профиль
                                        </Link>

                                    </li>



                                    <li className="nav-item">

                                        <button
                                            className="btn btn-link nav-link"
                                            onClick={logout}
                                        >
                                            Выйти
                                        </button>

                                    </li>


                                </>


                            ) : (

                                <>


                                    <li className="nav-item">

                                        <Link
                                            className="nav-link"
                                            to="/login"
                                        >
                                            Войти
                                        </Link>

                                    </li>



                                    <li className="nav-item">

                                        <Link
                                            className="nav-link"
                                            to="/register"
                                        >
                                            Регистрация
                                        </Link>

                                    </li>


                                </>

                            )
                        }


                    </ul>


                </div>


            </div>


        </nav>

    );

}


export default Navbar;
