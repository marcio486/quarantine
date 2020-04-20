import React,{Component} from 'react';
import {Provider} from 'react-redux'
import store from './store';
import ToDoList from './ToDoList'
import Counter from './Counter'
class App extends Component{
  render (){
    return (
      <Provider store = {store}>
        <div>
          <ToDoList></ToDoList>
          <Counter/>
        </div>
      </Provider>
    )
  }
}

export default App;
