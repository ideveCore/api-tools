python = import('python')

configure_file(
  input: 'apitools.in',
  output: 'apitools',
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
    'components/shortcuts/index.blp',
    'components/theme_switcher/index.blp',
    'pages/home/index.blp',
    'window.blp',
  ),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'],
)

gnome.compile_resources('apitools',
  'apitools.gresource.xml',
  dependencies: blueprints,
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

sources = [
  '__init__.py',
  'actions.py',
  'application.py',
  'components/theme_switcher/main.py',
  'pages/home/main.py',
  'main.py',
  'utils.py',
  'window.py',
]

install_data(sources, install_dir: moduledir)

# ===== Install components sources =====
install_subdir('components', install_dir: moduledir)

# ===== Install pages sources =====
install_subdir('pages', install_dir: moduledir)

# ===== Install assets sources =====
install_subdir('assets', install_dir: moduledir)
