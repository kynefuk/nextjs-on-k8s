import React, {useState} from 'react'
import {Table} from 'react-bootstrap';
import {Todo} from '../types/todo';
import styles from '../styles/TodoList.module.css'

export const TodoList = () => {
  const [todos, setTodos] = useState<Todo[]>([]);
  return (
    <Table striped bordered hover className={styles.table}>
      <thead>
        <tr>
          <th>ID</th>
          <th>Title</th>
          <th>Done</th>
        </tr>
      </thead>
      <tbody>
          {todos.map((todo) => {
            return (
              <tr key={todo.id}>
                <td>{todo.id}</td>
                <td>{todo.title}</td>
                <td>{todo.done}</td>
              </tr>
            )
        })}
      </tbody>
    </Table>
  )
}
