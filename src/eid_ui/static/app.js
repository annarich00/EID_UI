const state = {...window.initialState};
let selected;
const $ = (id) => document.getElementById(id);

function render() {
  $("distance").textContent = `${state.distance_km} km`;
  $("fuel").textContent = `${state.fuel_percent}%`;
  $("coverage").textContent = `${state.coverage_percent}%`;
  $("vulnerability").textContent = `${state.vulnerability_percent}%`;
  $("fuel-bar").style.width = `${state.fuel_percent}%`;
  $("coverage-bar").style.width = `${state.coverage_percent}%`;
  $("defender").style.left = `${Math.min(79, 32 + state.distance_km / 2)}%`;
}

async function choose(goal) {
  selected = await fetch(`/api/plan/${goal}`).then(response => response.json());
  document.querySelectorAll("[data-goal]").forEach(button => button.classList.toggle("selected", button.dataset.goal === goal));
  const sign = (number) => number > 0 ? `+${number}` : number;
  $("plan").innerHTML = `<strong>${selected.label}</strong><br>Projected change: ${sign(selected.distance_delta_km)} km distance · −${selected.fuel_cost_percent}% fuel · ${sign(selected.coverage_delta_percent)}% coverage · ${sign(selected.vulnerability_delta_percent)}% vulnerability.`;
  $("commit").disabled = false;
}

document.querySelectorAll("[data-goal]").forEach(button => button.addEventListener("click", () => choose(button.dataset.goal)));
$("commit").addEventListener("click", () => {
  if (!selected) return;
  state.distance_km = Math.max(0, state.distance_km + selected.distance_delta_km);
  state.fuel_percent = Math.max(0, state.fuel_percent - selected.fuel_cost_percent);
  state.coverage_percent = Math.max(0, Math.min(100, state.coverage_percent + selected.coverage_delta_percent));
  state.vulnerability_percent = Math.max(0, Math.min(100, state.vulnerability_percent + selected.vulnerability_delta_percent));
  $("event").textContent = selected.label;
  $("projection").textContent = "Projected state committed. Continue the perception–action cycle by selecting another goal.";
  render();
  $("commit").disabled = true;
});
render();
