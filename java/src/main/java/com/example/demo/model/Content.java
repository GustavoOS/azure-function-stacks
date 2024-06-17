package com.example.demo.model;

import com.example.demo.view.ContentDTO;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.SequenceGenerator;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Table(name = "content")
@Entity
@Data
public class Content {

  @Id
  @SequenceGenerator(name="content_id_seq",
      sequenceName="content_id_seq",
      allocationSize=1)
  @GeneratedValue(strategy = GenerationType.SEQUENCE,
      generator="content_id_seq")
  @Column(updatable = false)
  Long id;

  String title;

  String color;


  public ContentDTO toDTO() {
    return new ContentDTO(id, title, color);
  }
}
