import type { ReactNode } from "react";

interface Column<T> {
  key: keyof T | string;
  label: string;
  render?: (row: T) => ReactNode;
}

interface DataTableProps<T> {
  columns: Column<T>[];
  rows: T[];
  emptyMessage: string;
}

export function DataTable<T>({
  columns,
  rows,
  emptyMessage,
}: DataTableProps<T>) {
  return (
    <div className="table-card">
      <table className="data-table">
        <thead>
          <tr>
            {columns.map((column) => (
              <th key={String(column.key)}>{column.label}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.length === 0 ? (
            <tr>
              <td colSpan={columns.length} className="empty-state">
                {emptyMessage}
              </td>
            </tr>
          ) : (
            rows.map((row, rowIndex) => (
              <tr key={rowIndex}>
                {columns.map((column) => (
                  <td key={String(column.key)}>
                    {column.render
                      ? column.render(row)
                      : String(row[column.key as keyof T] ?? "")}
                  </td>
                ))}
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}
