%undefine _disable_source_fetch

Name:           python-typing_extensions
Version:        4.3.0
Release:        1%{?dist}
Summary:        Backported and experimental type hints for Python
URL:            https://python.org
Source0:        https://files.pythonhosted.org/packages/9e/1d/d128169ff58c501059330f1ad96ed62b79114a2eb30b8238af63a2e27f70/typing_extensions-4.3.0.tar.gz
License:        Python
BuildRequires:       python-devel
BuildArch:      noarch
%description
%{summary}.



%package -n python3-typing_extensions
Summary:        %{summary}

%description -n python3-typing_extensions
%{summary}

%prep
%autosetup -n typing_extensions-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files typing_extensions

%files -n python3-typing_extensions -f %{pyproject_files}
%doc README.md

%changelog
* Wed Sep 21 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 4.3.0-1.um36
- Initial Release

