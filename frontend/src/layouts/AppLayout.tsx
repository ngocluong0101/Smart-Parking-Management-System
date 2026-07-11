import { NavLink, Outlet } from "react-router-dom";

import { useTheme } from "../hooks/useTheme";

const navItems = [
  { to: "/dashboard", label: "Dashboard" },
  { to: "/camera-live", label: "Camera Live" },
  { to: "/vehicles", label: "Vehicle" },
  { to: "/history", label: "Parking History" },
  { to: "/statistics", label: "Statistics" },
  { to: "/settings", label: "Settings" },
  { to: "/users", label: "User Management" },
];

export function AppLayout() {
  const { theme, toggleTheme } = useTheme();

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div>
          <div className="brand">Smart Parking</div>
          <p className="sidebar-subtitle">Enterprise CV dashboard</p>
        </div>
        <nav className="nav">
          {navItems.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              className={({ isActive }) =>
                `nav-link${isActive ? " active" : ""}`
              }
            >
              {item.label}
            </NavLink>
          ))}
        </nav>
        <button className="theme-button" type="button" onClick={toggleTheme}>
          {theme === "dark" ? "Switch to Light Mode" : "Switch to Dark Mode"}
        </button>
      </aside>
      <main className="content">
        <header className="topbar">
          <div>
            <p className="eyebrow">Smart Parking Management System</p>
            <h1>Operations Dashboard</h1>
          </div>
          <div className="topbar-chip">Phase 8 frontend</div>
        </header>
        <Outlet />
      </main>
    </div>
  );
}
