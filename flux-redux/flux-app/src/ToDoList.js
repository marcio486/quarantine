import React, { Component } from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import * as todoActions from './actions/toDo'

class ToDoLista extends Component {
    constructor(props) {
        super(props);
        console.log(props)
    }

    state = {
        newTodoText: '',
    }

    addNewToDo = () => {
        this.props.addToDo(this.state.newTodoText)//Joga para o action
        this.setState({newTodoText : ''})
    };

    removeNewToDo = () => {
        this.props.RemoveToDo(this.state.newTodoText)//Joga para o action
        this.setState({newTodoText : ''})
    };

    render() {
        return (
            <div>
                <ul>
                    {this.props.todos.map(todo => (
                        <li key = {todo.id}> {todo.text},{todo.id}</li>
                        ))}
                </ul>
                <input
                    type="text"
                    value={this.state.newTodoText}
                    onChange = {(e) => this.setState({newTodoText : e.target.value})}
                />
                <button onClick={this.addNewToDo}>Adicionar item</button>
                <button onClick={this.removeNewToDo}>remover Item</button>

            </div>
        );
    }
}

const mapStateToProps = state => ({
    todos : state.toDos//toDos vem do index.js
});

const mapDispatchToProps = dispatch => bindActionCreators(todoActions, dispatch)// repassar ações como propriedas, para o componente enteder

export default connect(mapStateToProps, mapDispatchToProps)(ToDoLista);//