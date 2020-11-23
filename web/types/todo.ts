export interface Todo {
  id: number;
  title: string;
  done: boolean;
}

export interface TodoCreate {
  title: string;
  done: boolean;
}

export const initialData: TodoCreate = {
  title: "",
  done: false,
}