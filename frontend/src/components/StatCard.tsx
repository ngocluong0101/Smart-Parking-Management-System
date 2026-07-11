interface StatCardProps {
  label: string;
  value: string | number;
  hint?: string;
  tone?: "emerald" | "amber" | "cyan" | "rose";
}

export function StatCard({ label, value, hint, tone = "cyan" }: StatCardProps) {
  return (
    <section className={`stat-card tone-${tone}`}>
      <p className="stat-label">{label}</p>
      <div className="stat-value">{value}</div>
      {hint ? <p className="stat-hint">{hint}</p> : null}
    </section>
  );
}
