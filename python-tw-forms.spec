%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global srcname tw.forms

Name:           python-tw-forms
Version:        0.9.9
Release:        1%{?dist}
Summary:        Web Widgets for building and validating forms in ToscaWidgets
Group:          Development/Languages
# The javascript for the calendar widget is licensed under LGPLv2.1+
License:        MIT and LGPLv2+
URL:            http://toscawidgets.org/
Source0:        http://pypi.python.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-toscawidgets >= 0.9.6
Requires:       python-formencode >= 1.0.1

%description
tw.forms is a set of html and javascript widgets for the ToscaWidgets
framework.  They give authors basic html form elements as building blocks
for their own web pages and widgets.


%prep
%setup -q -n %{srcname}-%{version}


%build
chmod 0644 tw/forms/static/grid.css
sed -i 's/\r//' tw/forms/static/grid.css
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{python_sitelib}/*


%changelog
* Tue Jun 29 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.9-1
- 0.9.9
- replace %%define with %%global

* Thu Oct 01 2009 Luke Macken <lmacken@redhat.com> - 0.9.8-1
- 0.9.8

* Wed Aug 12 2009 Luke Macken <lmacken@redhat.com> - 0.9.7.2-1
- 0.9.7.2

* Wed Jun 10 2009 Luke Macken <lmacken@redhat.com> - 0.9.6-2
- Add a versioned ToscaWidgets requirement

* Thu Jun 04 2009 Luke Macken <lmacken@redhat.com> - 0.9.6-1
- Update to 0.9.6

* Mon Jun 01 2009 Luke Macken <lmacken@redhat.com> - 0.9.3-1
- Update to 0.9.3

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9.2-2
- Rebuild for Python 2.6

* Thu Oct 23 2008 Luke Macken <lmacken@redhat.com> - 0.9.2-1
- Update to tw.forms 0.9.2

* Sun Jul 27 2008 Toshio Kuratomi <toshio@fedoraproject.org> 0.9.1-1
- Initial Fedora Build
