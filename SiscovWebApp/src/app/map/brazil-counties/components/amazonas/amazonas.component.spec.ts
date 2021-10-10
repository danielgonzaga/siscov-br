import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AmazonasComponent } from './amazonas.component';

describe('AmazonasComponent', () => {
  let component: AmazonasComponent;
  let fixture: ComponentFixture<AmazonasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AmazonasComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AmazonasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
