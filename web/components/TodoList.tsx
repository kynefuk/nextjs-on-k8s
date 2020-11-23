import React from 'react'
import {Table} from 'react-bootstrap';
import {Todo} from '../types/todo';
import styles from '../styles/TodoList.module.css'
import useSWR from 'swr';

export const TodoList = () => {
  const {data} = useSWR<Todo[]>('http://localhost:7000/todos/');
  console.log(data)
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
        {data ?
          data.map((todo) => {
            return (
              <tr key={todo.id}>
                <td>{todo.id}</td>
                <td>{todo.title}</td>
                <td>{todo.done}</td>
              </tr>
            )
          })
        : null
        }
      </tbody>
    </Table>
  )
}
