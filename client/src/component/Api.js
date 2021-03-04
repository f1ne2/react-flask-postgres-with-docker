import React, { Component } from 'react';


export default class Ccomponent extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: []
        };
    }

    componentDidMount() {
        fetch("http://localhost:5000/categories/")
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        items: result.categories
                    });
                },
                (error) => {
                    this.setState({
                        isLoaded: true,
                        error
                    });
                }
            )
        fetch("http://localhost:5000/category/29", {
            method: 'delete'})
            .then((response) => {
                return response.json();
        })
            .then((data) => {
                console.log(data);
            })
            .catch((error) => {
                console.log(error)
            })
        let data = {data: "New"};
        fetch("http://localhost:5000/category/", {
            method: 'post',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify(data)})
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                console.log(data)
            });
        let put = {data: "Old"};
        let id = 30
        fetch("http://localhost:5000/category/"+ id, {
            method: 'put',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify(put)})
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                console.log(data)
            });

    }

    render() {
        const {error, isLoaded, items} = this.state;
        if (error) {
            return <p> Error {error.message}</p>
        } else if (!isLoaded) {
            return <p> Loading...</p>
        } else {
            return (
                <ul>
                    {items.map(item =>(
                        <li>
                            {item.id} {"   "}
                            {item.name}
                        </li>
                    ))}
                </ul>
            )}
    }
}


