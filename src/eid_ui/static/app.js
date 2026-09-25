let steps = [], index = 0, state, selected;
const $ = id => document.getElementById(id);
const clamp = (value, low, high) => Math.max(low, Math.min(high, value));

function render() {
  const step = steps[index];
  $("period").textContent = step.label;
  $("step-count").textContent = `Period ${index + 1} of ${steps.length}`;
  $("blue-status").textContent = step.blue_status;
  $("red-status").textContent = step.red_status;
  $("intelligence").textContent = step.intelligence;
  $("task").textContent = step.operator_task;
  $("distance").textContent = `${state.distance_km} km`;
  $("fuel").textContent = `${state.fuel_percent}%`;
  $("coverage").textContent = `${state.coverage_percent}%`;
  $("vulnerability").textContent = `${state.vulnerability_percent}%`;
  $("fuel-bar").style.width = `${state.fuel_percent}%`;
  $("coverage-bar").style.width = `${state.coverage_percent}%`;
  $("defender").style.left = `${clamp(28 + state.distance_km, 34, 80)}%`;
  $("event").textContent = index === 1 ? "Candidate: Most Time at Min" : "Scenario state";
  $("previous").disabled = index === 0;
  $("next").disabled = index === steps.length - 1;
  $("commit").disabled = true;
  selected = null;
  $("plan").textContent = "Select a goal to preview its trade-offs.";
  document.querySelectorAll("[data-goal]").forEach(button => button.classList.remove("selected"));
}

async function choose(goal) {
  selected = await fetch(`/api/plan/${goal}`).then(response => response.json());
  document.querySelectorAll("[data-goal]").forEach(button => button.classList.toggle("selected", button.dataset.goal === goal));
  const sign = number => number > 0 ? `+${number}` : number;
  $("plan").innerHTML = `<strong>${selected.label}</strong><br>Projected change: ${sign(selected.distance_delta_km)} km distance · −${selected.fuel_cost_percent}% fuel · ${sign(selected.coverage_delta_percent)}% coverage · ${sign(selected.vulnerability_delta_percent)}% vulnerability.`;
  $("commit").disabled = false;
}

function changePeriod(offset) {
  index += offset;
  const step = steps[index];
  state = {distance_km: step.distance_km, fuel_percent: step.fuel_percent, coverage_percent: step.coverage_percent, vulnerability_percent: step.vulnerability_percent};
  $("projection").textContent = "New scenario period loaded. Choose an end state to inspect a projected maneuver trade-off.";
  render();
}

document.querySelectorAll("[data-goal]").forEach(button => button.addEventListener("click", () => choose(button.dataset.goal)));
$("commit").addEventListener("click", () => {
  if (!selected) return;
  state.distance_km = Math.max(0, state.distance_km + selected.distance_delta_km);
  state.fuel_percent = Math.max(0, state.fuel_percent - selected.fuel_cost_percent);
  state.coverage_percent = clamp(state.coverage_percent + selected.coverage_delta_percent, 0, 100);
  state.vulnerability_percent = clamp(state.vulnerability_percent + selected.vulnerability_delta_percent, 0, 100);
  $("event").textContent = selected.label;
  $("projection").textContent = "Projected maneuver committed for this walkthrough period. Compare its visible constraint trade-offs before advancing.";
  render();
  $("event").textContent = selected.label;
});
$("previous").addEventListener("click", () => changePeriod(-1));
$("next").addEventListener("click", () => changePeriod(1));

fetch("/api/scenario").then(response => response.json()).then(data => {
  steps = data.steps;
  state = {...steps[0]};
  render();
});
