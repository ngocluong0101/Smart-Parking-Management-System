export function UserManagementPage() {
  return (
    <section className="panel">
      <div className="panel-header">
        <h3>User Management</h3>
        <span className="panel-badge">Role-based access</span>
      </div>
      <p className="muted-block">
        Admin and operator accounts will be managed here with JWT-backed access
        control.
      </p>
    </section>
  );
}
