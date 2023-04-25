import express, { Request, Response } from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';

const app = express();
app.use(bodyParser.json());
app.use(cors());

app.get('/', (req: Request, res: Response) => {
  res.send('Hello World!');
});

const port = 8000;
app.listen(port, () => {
  console.log(`http://localhost:${port}`);
});
