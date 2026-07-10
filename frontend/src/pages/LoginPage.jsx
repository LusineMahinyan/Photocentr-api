import { useState } from "react";
import { useNavigate } from "react-router-dom";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

import { loginUser } from "../api/auth";

function LoginPage() {

    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    async function handleSubmit(event) {

        event.preventDefault();

        try {

            const data = await loginUser(email, password);


            localStorage.setItem(
                "access_token",
                data.access_token
            );


            alert("Вход выполнен успешно!");


            navigate("/profile");


        } catch (error) {

            console.error(error);


            alert(
                JSON.stringify(
                    error.response?.data || error.message
                )
            );

        }

    }

    return (
        <>
            <Navbar />

            <div className="container py-5">

                <div className="row justify-content-center">

                    <div className="col-md-5">

                        <div className="card shadow-sm">

                            <div className="card-body">

                                <h2 className="text-center mb-4">
                                    Вход
                                </h2>

                                <form onSubmit={handleSubmit}>

                                    <div className="mb-3">

                                        <label className="form-label">
                                            Email
                                        </label>

                                        <input
                                            type="email"
                                            className="form-control"
                                            value={email}
                                            onChange={(e) => setEmail(e.target.value)}
                                        />

                                    </div>

                                    <div className="mb-4">

                                        <label className="form-label">
                                            Пароль
                                        </label>

                                        <input
                                            type="password"
                                            className="form-control"
                                            value={password}
                                            onChange={(e) => setPassword(e.target.value)}
                                        />

                                    </div>

                                    <button
                                        className="btn btn-warning w-100"
                                        type="submit"
                                    >
                                        Войти
                                    </button>

                                </form>

                            </div>

                        </div>

                    </div>

                </div>

            </div>

            <Footer />
        </>
    );
}

export default LoginPage;
