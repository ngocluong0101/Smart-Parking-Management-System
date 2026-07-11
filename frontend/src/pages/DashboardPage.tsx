import { useEffect, useState } from "react";

import { StatCard } from "../components/StatCard";
import {
  fetchActiveSessions,
  fetchDashboardSummary,
  fetchHistory,
} from "../services/dashboardService";
import type { DashboardSummary, ParkingSession } from "../types/api";

const fallbackSummary: DashboardSummary = {
  active_sessions: 18,
  total_sessions_today: 124,
  total_revenue_today: "560000",
  motorbike_count: 11,
  car_count: 7,
  other_vehicle_count: 0,
};

const fallbackHistory: ParkingSession[] = [
  {
    id: 1,
    vehicle_id: 1,
    parking_lot_id: 1,
    parking_fee_id: 1,
    plate_raw: "29A-12345",
    plate_normalized: "29A-12345",
    vehicle_type_snapshot: "car",
    status: "closed",
    check_in_time: new Date().toISOString(),
    check_out_time: new Date().toISOString(),
    duration_minutes: 90,
    total_fee: "20000",
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
  },
];

export function DashboardPage() {
  const [summary, setSummary] = useState<DashboardSummary>(fallbackSummary);
  const [recentSessions, setRecentSessions] =
    useState<ParkingSession[]>(fallbackHistory);

  useEffect(() => {
    fetchDashboardSummary()
      .then(setSummary)
      .catch(() => setSummary(fallbackSummary));
    fetchHistory(5)
      .then(setRecentSessions)
      .catch(() => setRecentSessions(fallbackHistory));
    fetchActiveSessions().catch(() => undefined);
  }, []);

  return (
    <div className="page-stack">
      <section className="hero-panel">
        <div>
          <p className="eyebrow">Realtime overview</p>
          <h2>Parking operations at a glance</h2>
          <p className="hero-copy">
            Monitor active vehicles, daily revenue, and session flow from a
            polished enterprise dashboard.
          </p>
        </div>
        <div className="hero-accent" />
      </section>

      <section className="stats-grid">
        <StatCard
          label="Active Sessions"
          value={summary.active_sessions}
          hint="Xe đang trong bãi"
          tone="cyan"
        />
        <StatCard
          label="Today Sessions"
          value={summary.total_sessions_today}
          hint="Tổng lượt xe"
          tone="emerald"
        />
        <StatCard
          label="Today Revenue"
          value={`${summary.total_revenue_today} VND`}
          hint="Doanh thu hôm nay"
          tone="amber"
        />
        <StatCard
          label="Cars"
          value={summary.car_count}
          hint="Ô tô"
          tone="rose"
        />
        <StatCard
          label="Motorbikes"
          value={summary.motorbike_count}
          hint="Xe máy"
          tone="cyan"
        />
        <StatCard
          label="Other"
          value={summary.other_vehicle_count}
          hint="Xe khác"
          tone="emerald"
        />
      </section>

      <section className="panel">
        <div className="panel-header">
          <h3>Recent Sessions</h3>
          <span className="panel-badge">Live sample</span>
        </div>
        <div className="mini-list">
          {recentSessions.map((session) => (
            <article key={session.id} className="mini-item">
              <div>
                <strong>{session.plate_normalized}</strong>
                <p>{session.vehicle_type_snapshot}</p>
              </div>
              <div className="mini-meta">
                <span>{session.status}</span>
                <span>{session.total_fee} VND</span>
              </div>
            </article>
          ))}
        </div>
      </section>
    </div>
  );
}
