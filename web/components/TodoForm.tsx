import React, {useState} from 'react'
import {Form, Button} from 'react-bootstrap'
import {initialData, TodoCreate} from '../types/todo'
import {useRouter} from 'next/router'

export const TodoForm = () => {
  const [todo, setTodo] = useState<TodoCreate>(initialData);
  const router = useRouter()

  const handleOnInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    const input = e.currentTarget.value;
    todo.title = input
    setTodo(todo)
  }

  const handleOnSubmit = async(e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log('hoge')
    try {
      const res = await fetch('http://localhost:7000/todos/', {method: "POST", body: JSON.stringify(todo)})
      router.push("/")
      if(res.status !== 200){
        throw new Error('Something Error');
      }
    } catch(err){
      console.error(err)
    }
  }

  return (
      <Form onSubmit={handleOnSubmit}>
        <Form.Group controlId="title">
          <Form.Label>Title</Form.Label>
          <Form.Control type="text" placeholder="title" />
          <Form.Text className="text-muted" onChange={handleOnInput}>Input todo title.</Form.Text>
        </Form.Group>
        <Button type="submit">
          Add
        </Button>
      </Form>
  )
}
