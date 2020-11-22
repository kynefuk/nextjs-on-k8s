import React from 'react'
import {Form} from 'react-bootstrap'

export const TodoForm = () => {
  return (
    <div>
      <Form>
        <Form.Group controlId="title">
          <Form.Label>Title</Form.Label>
          <Form.Control type="text" placeholder="title" />
          <Form.Text className="text-muted">Input todo title.</Form.Text>
        </Form.Group>
      </Form>
    </div>
  )
}
