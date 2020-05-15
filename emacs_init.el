;; INSTALL PACKAGES
;; --------------------------------------

(require 'package)
(add-to-list 'package-archives                                                                                                        
             '("elpy" . "http://jorgenschaefer.github.io/packages/"))   
(add-to-list 'package-archives
       '("melpa" . "https://melpa.org/packages/") t)

;; activate all packages
(package-initialize)

;; fetch the list of packages available 
(unless package-archive-contents
  (package-refresh-contents))

;; define list of packages to install
(defvar myPackages
  '(better-defaults
    material-theme
    exec-path-from-shell
    elpy
    pyenv-mode))

;; install all packages in list
(mapc #'(lambda (package)
    (unless (package-installed-p package)
      (package-install package)))
      myPackages)

;; Use shell's $PATH
(exec-path-from-shell-copy-env "PATH")

;; init.el ends here
;; If, on startup, packages can't be found, try `M-x pacakge-refresh-contents`.


;; BASIC CUSTOMIZATION
;; --------------------------------------

(setq inhibit-startup-message t)   ;; hide the startup message
(load-theme 'material t)           ;; load material theme
(global-linum-mode t)              ;; enable line numbers globally
(setq linum-format "%4d \u2502 ")  ;; format line number spacing
;; Allow hash to be entered  
(global-set-key (kbd "M-3") '(lambda () (interactive) (insert "#")))

;; define list of packages to install
(defvar myPackages
  '(better-defaults
    material-theme
    elpy))

(elpy-enable)

(add-hook 'python-mode-hook 'jedi:setup)
(setq jedi:complete-on-dot t)

(pyenv-mode)
;; (require 'conda)
;; (setq conda-env-home-directory (expand-file-name "~/.conda/envs"))
(setq python-shell-interpreter "ipython"
      python-shell-interpreter-args "-i --simple-prompt")
(venv-set-location "~/.conda/envs")

(require 'popwin)
(popwin-mode 1)

(define-key (current-global-map) (kbd "M-o") 'other-window)
(global-set-key (kbd "S-C-<left>") 'shrink-window-horizontally)
(global-set-key (kbd "S-C-<right>") 'enlarge-window-horizontally)
(global-set-key (kbd "S-C-<down>") 'shrink-window)
(global-set-key (kbd "S-C-<up>") 'enlarge-window)

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages
   (quote
    (jedi-direx rope-read-mode jedi virtualenvwrapper conda pyenv-mode-auto popwin popup-complete auto-complete deferred pyenv-mode elpy exec-path-from-shell material-theme better-defaults))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
