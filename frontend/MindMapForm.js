import React, { useState } from 'react';

const MindMapForm = ({ onSubmit, initialData = {} }) => {
  const [formData, setFormData] = useState({
    title: initialData.title || '',
    description: initialData.description || '',
  });

  const [formErrors, setFormErrors] = useState({});

  const validateForm = () => {
    let errors = {};
    if (!formData.title.trim()) errors.title = "Title is required";
    if (!formData.description.trim()) errors.description = "Description is required";
    setFormErrors(errors);
    return Object.keys(errors).length === 0;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormErrors({ ...formErrors, [name]: '' });
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!validateForm()) {
      alert('Please correct the errors before submitting.');
      return;
    }
    onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit} noValidate>
      <div>
        <label htmlFor="title">Title</label>
        <input
          type="text"
          id="title"
          name="title"
          value={formData.title}
          onChange={handleChange}
          required
        />
        {formErrors.title && <p style={{ color: 'red' }}>{formErrors.title}</p>}
      </div>
      <div>
        <label htmlFor="description">Description</label>
        <textarea
          id="description"
          name="description"
          value={formData.description}
          onChange={handleChange}
          required
        />
        {formErrors.description && <p style={{ color: 'red' }}>{formErrors.description}</p>}
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default MindMapForm;