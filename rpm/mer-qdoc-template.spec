Name:       mer-qdoc-template
Summary:    Mer Documentation QDoc templates
Version:    0.0.0
Release:    1
Group:      System/Libraries
License:    LGPLv2.1
URL:        https://github.com/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qmake
BuildRequires:  qt5-tools
BuildRequires:  qt5-qttools-qthelp-devel >= 5.2.0+git1
Requires:       qt5-qttools-qthelp-devel >= 5.2.0+git1

%description
%{summary}.

%package doc
Summary:    Mer Documentation QDoc templates documentation
Group:      System/Libraries

%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build
%qmake5
make %{?jobs:-j%jobs}
make docs %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%qmake5_install
make install_docs INSTALL_ROOT=%{buildroot}

%files
%defattr(-,root,root,-)
%dir %{_datadir}/doc/qt5/%{name}
%{_datadir}/qt5/mkspecs/features/mer-qdoc-template.prf
%{_datadir}/doc/qt5/%{name}/offline.qdocconf
%{_datadir}/doc/qt5/%{name}/common.qdocconf
%{_datadir}/doc/qt5/%{name}/fileextensions.qdocconf
%{_datadir}/doc/qt5/%{name}/mer-html-default-styles.qdocconf
%{_datadir}/doc/qt5/%{name}/mer-html-templates.qdocconf
%{_datadir}/doc/qt5/%{name}/images/breadcrumb.png
%{_datadir}/doc/qt5/%{name}/images/bullet_dn.png
%{_datadir}/doc/qt5/%{name}/images/bullet_gt.png
%{_datadir}/doc/qt5/%{name}/images/bullet_sq.png
%{_datadir}/doc/qt5/%{name}/images/bullet_up.png
%{_datadir}/doc/qt5/%{name}/style/offline.css

%files doc
%defattr(-,root,root,-)
%dir %{_datadir}/doc/%{name}
%{_datadir}/doc/%{name}/mer-qdoc-template.qch
