declare class Worker {
  constructor(url: string | URL, options?: WorkerOptions);
}

interface WorkerOptions {
  type?: "classic" | "module";
  credentials?: "omit" | "same-origin" | "include";
  name?: string;
}
