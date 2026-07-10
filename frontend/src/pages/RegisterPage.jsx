import { useState } from "react";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

import { registerUser } from "../api/auth";

function RegisterPage() {
    const [formData, setFormData] = useState({
        full_name: "",
        email: "",
        phone: "",
        password: "",
        confirm_password: "",
    });

    function handleChange(event) {
        setFormData({
            ...formData,
            [event.target.name]: event.target.value,
        });
    }

    async function handleSubmit(event) {
        event.preventDefault();

        try {
            const result = await registerUser(formData);

            console.log(result);

            alert("Регистрация успешна!");
        } catch (error) {
            console.error(
                "Ошибка регистрации:",
                error.response?.data || error.message
            );

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
                    <div className="col-md-6">

                        <div className="card shadow-sm">

                            <div className="card-body">

                                <h2 className="text-center mb-4">
                                    Регистрация
                                </h2>

                                <form onSubmit={handleSubmit}>

                                    <div className="mb-3">
                                        <label className="form-label">
                                            Имя
                                        </label>

                                        <input
                                            type="text"
                                            className="form-control"
                                            name="full_name"
                                            value={formData.full_name}
                                            onChange={handleChange}
                                        />
                                    </div>

                                    <div className="mb-3">
                                        <label className="form-label">
                                            Email
                                        </label>

                                        <input
                                            type="email"
                                            className="form-control"
                                            name="email"
                                            value={formData.email}
                                            onChange={handleChange}
                                        />
                                    </div>

                                    <div className="mb-3">
                                        <label className="form-label">
                                            Телефон
                                        </label>

                                        <input
                                            type="text"
                                            className="form-control"
                                            name="phone"
                                            value={formData.phone}
                                            onChange={handleChange}
                                        />
                                    </div>

                                    <div className="mb-3">
                                        <label className="form-label">
                                            Пароль
                                        </label>

                                        <input
                                            type="password"
                                            className="form-control"
                                            name="password"
                                            value={formData.password}
                                            onChange={handleChange}
                                        />
                                    </div>

                                    <div className="mb-4">
                                        <label className="form-label">
                                            Подтвердите пароль
                                        </label>

                                        <input
                                            type="password"
                                            className="form-control"
                                            name="confirm_password"
                                            value={formData.confirm_password}
                                            onChange={handleChange}
                                        />
                                    </div>

                                    <button
                                        className="btn btn-warning w-100"
                                        type="submit"
                                    >
                                        Создать аккаунт
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

export default RegisterPage;
