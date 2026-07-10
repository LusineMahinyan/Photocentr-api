import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

import { getMe } from "../api/users";


function ProfilePage() {


    const [user, setUser] = useState(null);


    useEffect(() => {

        loadUser();

    }, []);



    async function loadUser() {

        try {

            const data = await getMe();

            console.log(
                "Пользователь:",
                data
            );

            setUser(data);


        } catch (error) {

            console.error(
                error.response?.data || error.message
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


                                <h1 className="text-center mb-4">
                                    👤 Профиль
                                </h1>



                                {
                                    user ? (

                                        <>


                                            <h3 className="text-center">
                                                {user.full_name}
                                            </h3>


                                            <hr />


                                            <p>
                                                📧 Email:
                                                {" "}
                                                {user.email}
                                            </p>


                                            <p>
                                                📱 Телефон:
                                                {" "}
                                                {user.phone}
                                            </p>


                                            <div className="text-center mt-4">


                                                <Link
                                                    to="/orders"
                                                    className="btn btn-warning"
                                                >
                                                    📦 Мои заказы
                                                </Link>


                                            </div>


                                        </>


                                    ) : (


                                        <div className="text-center">

                                            Загрузка...

                                        </div>


                                    )

                                }


                            </div>


                        </div>


                    </div>


                </div>


            </div>


            <Footer />

        </>

    );

}


export default ProfilePage;
