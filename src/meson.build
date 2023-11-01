python = import('python')

configure_file(
  input: 'api-tools.in',
  output: 'api-tools',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
)

configure_file(
  input: 'define.in',
  output: 'define.py',
  configuration: conf,
  install: true,
  install_dir: moduledir
)

launcher = join_paths(meson.project_build_root(), 'src', meson.project_name())
run_target('run',
  command: [launcher]
)

blueprints = custom_target('blueprints',
  input: files(
    'components/theme_switcher/index.blp',
    'window.blp',
  ),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'],
)

gnome.compile_resources('api-tools',
  'api-tools.gresource.xml',
  dependencies: blueprints,
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

sources = [
  'components/theme_switcher/main.py',
  '__init__.py',
  'actions.py',
  'application.py',
  'main.py',
  'window.py',
]

install_data(sources, install_dir: moduledir)

# ===== Install components sources =====
install_subdir('components', install_dir: moduledir)

# ===== Install assets sources =====
install_subdir('assets', install_dir: moduledir)
