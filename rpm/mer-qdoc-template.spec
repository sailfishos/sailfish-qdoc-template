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
%dir %{_datadir}/%{name}
%{_datadir}/qt5/mkspecs/features/mer-qdoc-template.prf
%{_datadir}/%{name}/offline.qdocconf
%{_datadir}/%{name}/common.qdocconf
%{_datadir}/%{name}/fileextensions.qdocconf
%{_datadir}/%{name}/qt-cpp-defines.qdocconf
%{_datadir}/%{name}/mer-html-default-styles.qdocconf
%{_datadir}/%{name}/mer-html-templates.qdocconf
%{_datadir}/%{name}/images/breadcrumb.png
%{_datadir}/%{name}/images/bullet_dn.png
%{_datadir}/%{name}/images/bullet_gt.png
%{_datadir}/%{name}/images/bullet_sq.png
%{_datadir}/%{name}/images/bullet_up.png
%{_datadir}/%{name}/style/offline.css

%files doc
%defattr(-,root,root,-)
%dir %{_datadir}/doc/%{name}
%{_datadir}/doc/%{name}/mer-qdoc-template.qch
