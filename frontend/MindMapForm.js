import React, { useState, useCallback } from 'react';

const MindMapForm = ({ onSubmit, initialData = {} }) => {
  const [formData, setFormData] = useState({
    title: initialData.title || '',
    description: initialData.description || '',
  });

  const [formErrors, setFormErrors] = useState({});

  const validateForm = useCallback(() => {
    let errors = {};
    if (!formData.title.trim()) errors.title = "Title is required";
    if (!formData.description.trim()) errors.description = "Description is required";
    setFormErrors(errors);
    return Object.keys(errors).length === 0;
  }, [formData.title, formData.description]);

  const handleChange = useCallback((e) => {
    const { name, value } = e.target;
    setFormErrors((prevErrors) => ({ ...prevErrors, [name]: '' }));
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  }, []);

  const handleBlur = useCallback((event) => {
    const { name, value } = event.target;
    const capitalized = capitalizeFirstLetter(value);
    setFormData((prevData) => ({ ...prevData, [name]: capitalized }));
  }, []);

  const capitalizeFirstLetter = (string) => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };

  const handleSubmit = useCallback((e) => {
    e.preventDefault();
    if (!validateForm()) {
      alert('Please correct the errors before submitting.');
      return;
    }
    onSubmit(formData);
  }, [formData, validateForm, onSubmit]);

  return (
    <form onSubmit={handleSubmit} noValidate>
      <FormField
        label="Title"
        type="text"
        name="title"
        value={formData.title}
        onChange={handleChange}
        onBlur={handleBlur}
        error={formErrors.title}
      />
      <FormField
        label="Description"
        type="textarea"
        name="description"
        value={formData.description}
        onChange={handleChange}
        onBlur={handleBlur}
        error={formErrors.description}
      />
      <button type="submit">Submit</button>
    </form>
  );
};

const FormField = ({ label, type, name, value, onChange, onBlur, error }) => (
  <div>
    <label htmlFor={name}>{label}</label>
    {type === "textarea" ? (
      <textarea
        id={name}
        name={name}
        value={value}
        onChange={onChange}
        onBlur={onBlur}
        required
      />
    ) : (
      <input
        type={type}
        id={name}
        name={name}
        value={value}
        onChange={onChange}
        onBlur={onBlur}
        required
      />
    )}
    {error && <p style={{ color: 'red' }}>{error}</p>}
  </div>
);

export default MindMapForm;