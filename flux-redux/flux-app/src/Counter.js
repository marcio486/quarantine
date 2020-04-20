import React from 'react';
import { connect } from 'react-redux';

const Counter = (props) => (
    <h2>fucniona?{props.todos.length}</h2>
);

const mapStateToProps = state => ({
    todos:  state.toDos//toDos vem do index.js
})

export default connect(mapStateToProps)(Counter);