export function LoginPage() {
  return (
    <div className="auth-shell">
      <section className="auth-card">
        <p className="eyebrow">Secure access</p>
        <h1>Login to Smart Parking</h1>
        <p>Enterprise-grade dashboard for operators and admins.</p>
        <form className="auth-form">
          <label>
            Username
            <input type="text" placeholder="admin" />
          </label>
          <label>
            Password
            <input type="password" placeholder="••••••••" />
          </label>
          <button type="button">Sign In</button>
        </form>
      </section>
    </div>
  );
}
