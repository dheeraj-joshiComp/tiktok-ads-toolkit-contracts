
(() => {
  const rows = [...document.querySelectorAll('[data-action-row]')];
  const search = document.querySelector('#action-search');
  const method = document.querySelector('#method-filter');
  const category = document.querySelector('#category-filter');
  const count = document.querySelector('#result-count');
  const empty = document.querySelector('#empty-state');
  if (!rows.length || !search || !method || !category || !count || !empty) return;
  const update = () => {
    const query = search.value.trim().toLowerCase();
    let visible = 0;
    rows.forEach((row) => {
      const show = (!query || row.dataset.search.includes(query)) &&
        (!method.value || row.dataset.method === method.value) &&
        (!category.value || row.dataset.category === category.value);
      row.hidden = !show;
      if (show) visible += 1;
    });
    count.textContent = `${visible} shown`;
    empty.hidden = visible !== 0;
  };
  [search, method, category].forEach((control) => control.addEventListener('input', update));
})();
